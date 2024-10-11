# Extracted from ./data/repos/scrapy/scrapy/commands/genspider.py
ScrapyCommand.add_options(self, parser)
parser.add_argument("-l", "--list", dest="list", action="store_true",
                    help="List available templates")
parser.add_argument("-e", "--edit", dest="edit", action="store_true",
                    help="Edit spider after creating it")
parser.add_argument("-d", "--dump", dest="dump", metavar="TEMPLATE",
                    help="Dump template to standard output")
parser.add_argument("-t", "--template", dest="template", default="basic",
                    help="Uses a custom template.")
parser.add_argument("--force", dest="force", action="store_true",
                    help="If the spider already exists, overwrite it with the template")
