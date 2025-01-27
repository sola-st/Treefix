# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

# Read the full spec file, used for everything
with open(FLAGS.spec_file, 'r') as spec_file:
    tag_spec = yaml.safe_load(spec_file)

# Get existing partial contents
partials = gather_existing_partials(FLAGS.partial_dir)

# Abort if spec.yaml is invalid
schema = yaml.safe_load(SCHEMA_TEXT)
v = TfDockerTagValidator(schema, partials=partials)
if not v.validate(tag_spec):
    eprint('> Error: {} is an invalid spec! The errors are:'.format(
        FLAGS.spec_file))
    eprint(yaml.dump(v.errors, indent=2))
    exit(1)
tag_spec = v.normalized(tag_spec)

# Assemble tags and images used to build them
all_tags = assemble_tags(tag_spec, FLAGS.arg, FLAGS.release, partials)

# Empty Dockerfile directory if building new Dockerfiles
if FLAGS.construct_dockerfiles:
    eprint('> Emptying Dockerfile dir "{}"'.format(FLAGS.dockerfile_dir))
    shutil.rmtree(FLAGS.dockerfile_dir, ignore_errors=True)
    mkdir_p(FLAGS.dockerfile_dir)

# Set up Docker helper
dock = docker.from_env()

# Login to Docker if uploading images
if FLAGS.upload_to_hub:
    if not FLAGS.hub_username:
        eprint('> Error: please set --hub_username when uploading to Dockerhub.')
        exit(1)
    if not FLAGS.hub_repository:
        eprint(
            '> Error: please set --hub_repository when uploading to Dockerhub.')
        exit(1)
    if not FLAGS.hub_password:
        eprint('> Error: please set --hub_password when uploading to Dockerhub.')
        exit(1)
    dock.login(
        username=FLAGS.hub_username,
        password=FLAGS.hub_password,
    )

# Each tag has a name ('tag') and a definition consisting of the contents
# of its Dockerfile, its build arg list, etc.
failed_tags = []
succeeded_tags = []
for tag, tag_defs in all_tags.items():
    for tag_def in tag_defs:
        eprint('> Working on {}'.format(tag))

        if FLAGS.exclude_tags_matching and re.match(FLAGS.exclude_tags_matching,
                                                    tag):
            eprint('>> Excluded due to match against "{}".'.format(
                FLAGS.exclude_tags_matching))
            continue

        if FLAGS.only_tags_matching and not re.match(FLAGS.only_tags_matching,
                                                     tag):
            eprint('>> Excluded due to failure to match against "{}".'.format(
                FLAGS.only_tags_matching))
            continue

        # Write releases marked "is_dockerfiles" into the Dockerfile directory
        if FLAGS.construct_dockerfiles and tag_def['is_dockerfiles']:
            path = os.path.join(FLAGS.dockerfile_dir,
                                tag_def['dockerfile_subdirectory'],
                                tag + '.Dockerfile')
            eprint('>> Writing {}...'.format(path))
            if not FLAGS.dry_run:
                mkdir_p(os.path.dirname(path))
                with open(path, 'w') as f:
                    f.write(tag_def['dockerfile_contents'])

      # Don't build any images for dockerfile-only releases
        if not FLAGS.build_images:
            continue

        # Only build images for host architecture
        proc_arch = platform.processor()
        is_x86 = proc_arch.startswith('x86')
        if (is_x86 and any(arch in tag for arch in ['ppc64le']) or
            not is_x86 and proc_arch not in tag):
            continue

        # Generate a temporary Dockerfile to use to build, since docker-py
        # needs a filepath relative to the build context (i.e. the current
        # directory)
        dockerfile = os.path.join(FLAGS.dockerfile_dir, tag + '.temp.Dockerfile')
        if not FLAGS.dry_run:
            with open(dockerfile, 'w') as f:
                f.write(tag_def['dockerfile_contents'])
        eprint('>> (Temporary) writing {}...'.format(dockerfile))

        repo_tag = '{}:{}'.format(FLAGS.repository, tag)
        eprint('>> Building {} using build args:'.format(repo_tag))
        for arg, value in tag_def['cli_args'].items():
            eprint('>>> {}={}'.format(arg, value))

        # Note that we are NOT using cache_from, which appears to limit
        # available cache layers to those from explicitly specified layers. Many
        # of our layers are similar between local builds, so we want to use the
        # implied local build cache.
        tag_failed = False
        image, logs = None, []
        if not FLAGS.dry_run:
            try:
                # Use low level APIClient in order to stream log output
                resp = dock.api.build(
                    timeout=FLAGS.hub_timeout,
                    path='.',
                    nocache=FLAGS.nocache,
                    dockerfile=dockerfile,
                    buildargs=tag_def['cli_args'],
                    tag=repo_tag)
                last_event = None
                image_id = None
                # Manually process log output extracting build success and image id
                # in order to get built image
                while True:
                    try:
                        output = next(resp).decode('utf-8')
                        json_output = json.loads(output.strip('\r\n'))
                        if 'stream' in json_output:
                            eprint(json_output['stream'], end='')
                            match = re.search(r'(^Successfully built |sha256:)([0-9a-f]+)$',
                                              json_output['stream'])
                            if match:
                                image_id = match.group(2)
                            last_event = json_output['stream']
                            # collect all log lines into the logs object
                            logs.append(json_output)
                    except StopIteration:
                        eprint('Docker image build complete.')
                        break
                    except ValueError:
                        eprint('Error parsing from docker image build: {}'.format(output))
          # If Image ID is not set, the image failed to built properly. Raise
          # an error in this case with the last log line and all logs
                if image_id:
                    image = dock.images.get(image_id)
                else:
                    raise docker.errors.BuildError(last_event or 'Unknown', logs)

                # Run tests if requested, and dump output
                # Could be improved by backgrounding, but would need better
                # multiprocessing support to track failures properly.
                if FLAGS.run_tests_path:
                    if not tag_def['tests']:
                        eprint('>>> No tests to run.')
                    for test in tag_def['tests']:
                        eprint('>> Testing {}...'.format(test))
                        container, = dock.containers.run(
                            image,
                            '/tests/' + test,
                            working_dir='/',
                            log_config={'type': 'journald'},
                            detach=True,
                            stderr=True,
                            stdout=True,
                            volumes={
                                FLAGS.run_tests_path: {
                                    'bind': '/tests',
                                    'mode': 'ro'
                                }
                            },
                            runtime=tag_def['test_runtime']),
                        ret = container.wait()
                        code = ret['StatusCode']
                        out = container.logs(stdout=True, stderr=False)
                        err = container.logs(stdout=False, stderr=True)
                        container.remove()
                        if out:
                            eprint('>>> Output stdout:')
                            eprint(out.decode('utf-8'))
                        else:
                            eprint('>>> No test standard out.')
                        if err:
                            eprint('>>> Output stderr:')
                            eprint(err.decode('utf-8'))
                        else:
                            eprint('>>> No test standard err.')
                        if code != 0:
                            eprint('>> {} failed tests with status: "{}"'.format(
                                repo_tag, code))
                            failed_tags.append(tag)
                            tag_failed = True
                            if FLAGS.stop_on_failure:
                                eprint('>> ABORTING due to --stop_on_failure!')
                                exit(1)
                        else:
                            eprint('>> Tests look good!')

            except docker.errors.BuildError as e:
                eprint('>> {} failed to build with message: "{}"'.format(
                    repo_tag, e.msg))
                eprint('>> Build logs follow:')
                log_lines = [l.get('stream', '') for l in e.build_log]
                eprint(''.join(log_lines))
                failed_tags.append(tag)
                tag_failed = True
                if FLAGS.stop_on_failure:
                    eprint('>> ABORTING due to --stop_on_failure!')
                    exit(1)

        # Clean temporary dockerfiles if they were created earlier
            if not FLAGS.keep_temp_dockerfiles:
                os.remove(dockerfile)

      # Upload new images to DockerHub as long as they built + passed tests
        if FLAGS.upload_to_hub:
            if not tag_def['upload_images']:
                continue
            if tag_failed:
                continue

            eprint('>> Uploading to {}:{}'.format(FLAGS.hub_repository, tag))
            if not FLAGS.dry_run:
                p = multiprocessing.Process(
                    target=upload_in_background,
                    args=(FLAGS.hub_repository, dock, image, tag))
                p.start()

        if not tag_failed:
            succeeded_tags.append(tag)

if failed_tags:
    eprint(
        '> Some tags failed to build or failed testing, check scrollback for '
        'errors: {}'.format(','.join(failed_tags)))
    exit(1)

eprint('> Writing built{} tags to standard out.'.format(
    ' and tested' if FLAGS.run_tests_path else ''))
for tag in succeeded_tags:
    print('{}:{}'.format(FLAGS.repository, tag))
