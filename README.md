<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://user-images.githubusercontent.com/78688623/160965843-31dd0dd6-ad6f-4167-8e22-1a5d37f91a38.jpg" width="128" height="128">
  </a>

<!-- ABOUT -->
## About

**MarauderMC** is a custom [**Discord**](https://discord.com/) bot solution developed within [**discord.py**](https://github.com/Rapptz/discord.py), an API wrapper written in Python.

The management of an online gaming community, **MarauderMC**, comissioned me to develop and setup a bespoke bot application for their Discord guild to handle support and verification matters.

Such application was developed promptly and delivered upon key client needs of allowing guild members to partake in reaction functionality and ensuring that tickets workflow was as efficient as possible for support staff.

### Built With
* [Python](https://www.python.org/)

<!-- TABLE OF CONTENTS -->
## Table of Contents
* [About](#about)
  * [Built With](#built-with)
* [Installation](#installation)
* [Commands](#commands)
* [License](#license)

<!-- INSTALLATION -->
## Installation
To run **MarauderMC**, download this repository and ensure that you are running `Python 3.5.3` or higher and have `discord.py` installed:

`python3 -m pip install -U discord.py`

Then set your bot token: `token=''` within `config.py`, run `maraudermc.py` and away you go!

<!-- COMMANDS -->
## Commands
| Command Usage | Description | Permission |
| ------- | ----------- | ----------- |
| `!clickVerification` | **MarauderMC** will output an embed to be used with verification functionality. | administrator |
| `!close` | **MarauderMC** will close the current ticket and use Toptal API to output ticket log. | config.ticketsSupportRole |
| `!tickets` | **MarauderMC** will output an embed to be used with tickets functionality. | administrator |

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/paulranshaw/MarauderMC
[contributors-url]: https://github.com/paulranshaw/MarauderMC/graphs/contributors
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/paulranshaw