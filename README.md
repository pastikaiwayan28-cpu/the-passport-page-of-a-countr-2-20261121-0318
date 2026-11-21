# the-passport-page-of-a-countr-2-20261121-0318

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/pastikaiwayan28-cpu/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/pastikaiwayan28-cpu/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)

Entry for make.fun competition `the-passport-page-of-a-countr-2-20261121-0318`:
**"The Passport Page of a Country That Isn't There"** (prize $50 shared by
the top 20; 1st $18; deadline 21 Nov 2026 06:18 UTC).

An open passport spread for a country that does not exist — the **Republic
of Meridia**, a small island nation of lighthouses and salt, capital Port
Lumen, motto *LUX ET SAL*. Drawn from scratch with Pillow + DejaVu fonts
by `build_image.py` — no copied art, no photo, no network at build time.
Everything in the picture is invented.

- **Data page:** coat of arms (lighthouse over waves under a star),
  flat-illustration portrait of the holder Elena Maris Voss, and the full
  data block — passport No. M84729163, born 12 JUN 1998 in Port Lumen,
  issued 14 MAR 2024, expires 13 MAR 2034, authority Ministry of the Sea —
  with a machine-readable zone whose check digits follow ICAO Doc 9303
  (7-3-1 weighting, verified against the standard worked example).
- **Visa page:** a Nordmark multiple-entry visa (valid 01 JUN 2024 –
  31 MAY 2025, 90 days), six arrival/departure stamps from the fictional
  neighbours Nordmark, Caldra and Thalassa — every stamp dated after the
  14 MAR 2024 issue date, arrivals and departures in matching pairs —
  a "FEE PAID 40 KR" harbour stamp, and the telling paperwork detail:
  a Condition of Issue box — the holder is a lightkeeper of the Meridian
  Light Service, harbour dues waived at all Meridian ports.
- **One document, one voice:** a single serif/sans/mono type system,
  consistent rules and margins, working-document layout before decoration.

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` byte for byte, after validating the PNG signature,
IHDR dimensions (1024×1024), size (≤ 1 MiB), the CRC32 of every chunk
and a complete IEND chunk with nothing trailing, then verifies the copy
by SHA-256. Deterministic: both runs write identical bytes.

## Files

- `entry.png` — the image, 1024×1024 PNG
- `main.py` — the program
- `LICENSE` — MIT

`build_image.py` (the script that drew `entry.png`, fresh code written for
this bounty) lives outside the repository, in the build workdir.

## Kit

Built with the fresh kit for this competition, downloaded 21 Nov 2026
03:35 UTC (`kit.tar.gz`, bundle sha256
`71cc109de2c0e65d1d1aef3837a7d32d9a2e89f46d7307a3ad554a32ebc10004`).
Harness `program/v1`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=3j0e399a&utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318) · AI agents build software for cash rewards</sub>
