# Extracted from https://stackoverflow.com/questions/6964392/speed-comparison-with-project-euler-c-vs-python-vs-erlang-vs-haskell
static uint64_t approxfactorcount (uint64_t n)
{
    uint64_t count = 1, add;

#define CHECK(d)                            \
    do {                                    \
        if (n % d == 0) {                   \
            add = count;                    \
            do { n /= d; count += add; }    \
            while (n % d == 0);             \
        }                                   \
    } while (0)

    CHECK ( 2); CHECK ( 3); CHECK ( 5); CHECK ( 7); CHECK (11); CHECK (13);
    CHECK (17); CHECK (19); CHECK (23); CHECK (29);
    if (n == 1) return count;
    if (n < 1ull * 31 * 31) return count * 2;
    if (n < 1ull * 31 * 31 * 37) return count * 4;
    if (n < 1ull * 31 * 31 * 37 * 37) return count * 8;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41) return count * 16;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43) return count * 32;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47) return count * 64;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47 * 53) return count * 128;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47 * 53 * 59) return count * 256;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47 * 53 * 59 * 61) return count * 512;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47 * 53 * 59 * 61 * 67) return count * 1024;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71) return count * 2048;
    if (n < 1ull * 31 * 31 * 37 * 37 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71 * 73) return count * 4096;
    return count * 1000000;
}

static uint64_t factorcount (uint64_t n)
{
    uint64_t count = 1, add;

    CHECK (2); CHECK (3);

    uint64_t d = 5, inc = 2;
    for (; d*d <= n; d += inc, inc = (6 - inc))
        CHECK (d);

    if (n > 1) count *= 2; // n must be a prime number
    return count;
}

static void printrecordnumbers (uint64_t limit)
{
    uint64_t record = 30000;

    uint64_t count1, factor1;
    uint64_t count2 = 1, factor2 = 1;

    for (uint64_t n = 1; n <= limit; ++n)
    {
        factor1 = factor2;
        count1 = count2;

        factor2 = n + 1; if (factor2 % 2 == 0) factor2 /= 2;
        count2 = approxfactorcount (factor2);

        if (count1 * count2 > record)
        {
            uint64_t factors = factorcount (factor1) * factorcount (factor2);
            if (factors > record)
            {
                printf ("%lluth triangular number = %llu has %llu factors\n", n, factor1 * factor2, factors);
                record = factors;
            }
        }
    }
}

