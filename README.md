# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/shusay12/makefun-u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/shusay12/makefun-u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/competitions/u-azazex-last-text-at-one-percent-ba9fc876)

The funniest final text message a dying phone sends at one percent battery,
in the voice of the dying phone itself.

## Entry

> 1% left. The 47 open tabs outlived me, and I never read a single one. I die as I lived: buffering, overheating, ignored.

## How it works

`main.py` (Python 3.13 stdlib only, no network) writes the entry to
`/output/entry.txt`. The output is deterministic: two runs produce
byte-identical files.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
