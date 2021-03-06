# Advent of Code 2021 (Python) 🎄

<div align="center">

| Day                                        | 1   | 2   | 📃                           | ⏲️   |
| ------------------------------------------ | :-: | :-: | :--------------------------: | :--: |
| [01](https://adventofcode.com/2021/day/1)  | ⭐  | ⭐  | **[day01.py](src/day01.py)** | 🟢🟢 |
| [02](https://adventofcode.com/2021/day/2)  | ⭐  | ⭐  | **[day02.py](src/day02.py)** | 🟢🟢 |
| [03](https://adventofcode.com/2021/day/3)  | ⭐  | ⭐  | **[day03.py](src/day03.py)** | 🟢🟢 |
| [04](https://adventofcode.com/2021/day/4)  | ⭐  | ⭐  | **[day04.py](src/day04.py)** | 🟢🟢 |
| [05](https://adventofcode.com/2021/day/5)  | ⭐  | ⭐  | **[day05.py](src/day05.py)** | 🟢🟡 |
| [06](https://adventofcode.com/2021/day/6)  | ⭐  | ⭐  | **[day06.py](src/day06.py)** | 🟢🟢 |
| [07](https://adventofcode.com/2021/day/7)  | ⭐  | ⭐  | **[day07.py](src/day07.py)** | 🟢🟢 |
| [08](https://adventofcode.com/2021/day/8)  | ⭐  |     | **[day08.py](src/day08.py)** | 🟢   |
| [09](https://adventofcode.com/2021/day/9)  | ⭐  |     | **[day09.py](src/day09.py)** | 🟢   |
| [10](https://adventofcode.com/2021/day/10) | ⭐  | ⭐  | **[day10.py](src/day10.py)** | 🟢🟢 |
| [11](https://adventofcode.com/2021/day/11) |     |     |                              |      |
| [12](https://adventofcode.com/2021/day/12) |     |     |                              |      |
| [13](https://adventofcode.com/2021/day/13) |     |     |                              |      |
| [14](https://adventofcode.com/2021/day/14) | ⭐  |     | **[day14.py](src/day14.py)** | 🟢   |

<sub>🟢 < 1 day | 🟡 1÷7 days | 🟠 = 7÷30 days | 💤 > 30 days</sub>

</div>

## How to run

`Python 3.8` and `poetry` required. From the root folder:

````bash
# Prepare the virtualenv (will be placed at .venv/), only needed the first time
poetry install
# Activate the virtualenv
source .venv/bin/activate
# Run the script for day 01
python3.8 src/day01.py
````

The script `src/day00_template.py` can be used as a template, simply copy and rename it `day[DD].py`

Scripts are configured to automatically download puzzle inputs. To setup this, continue to the section below

### Setup (automatic input download)

To get and set your credentials: login into [AoC](https://adventofcode.com/) and open the Web Developer Tools (`CTRL+SHIFT+I`) in your browser. Go to the Storage tab (or Application/Storage in Chrome) and copy the value of your `session` cookie. Paste it into the `aoc_cookie` entry in the configuration file (`config.json`). Notice that in the same file you can also set the year to use this repository for a different year

**Important**: do not commit the `config.json` file as it contains your personal cookie. Run `git update-index --assume-unchanged config.json` to prevent git from tracking the file

## Happy holidays playlist! 🎁

["Ding Dong Merrily on High"](https://www.youtube.com/watch?v=zJbRURK3zWo) by *Tom Bombadil*

["Here codes Santa Claus"](https://www.youtube.com/watch?v=ysxlUmLOttQ) by *Gene Poetry*

["It's the Most Wonderful Thyme of the Year [at Scarborough Fair]"](https://www.youtube.com/watch?v=-BakWVXHSug) by *Simon & Garfunkel*

