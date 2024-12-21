<center>

# MarzneshinIpLimit

<b>Limiting the number of active users with IP for [Marzneshin](https://github.com/marzneshin/marzneshin)</b><sub> (with xray logs)</sub><br>
Supports both IPv4 and IPv6
<sub>(Tested on Ubuntu 22.04 & 24.04, Fedora 39 & 40)</sub>

</center>

<hr>

## Table of Contents

- [Installation](#installation)
- [Telegram Bot Commands](#telegram-bot-commands)
- [Common Issues and Solutions](#common-issues-and-solutions)
- [Using Cron Jobs](#using-cron-jobs)
- [Build](#build)
- [Donations](#donations)

## Installation

Installation with docker:

Install docker

```bash
curl -fsSL https://get.docker.com | sh
```

```bash
mkdir /opt/marzneshiniplimit
cd /opt/marzneshiniplimit
```

```bash
curl -O -L "https://raw.githubusercontent.com/kizil-aslan/MarzneshinIpLimit/main/config.json";
```

```bash
curl -O -L "https://raw.githubusercontent.com/kizil-aslan/MarzneshinIpLimit/main/app.log";
```

```bash
curl -O -L "https://raw.githubusercontent.com/kizil-aslan/MarzneshinIpLimit/main/docker-compose.yml";
```

```bash
docker compose up -d
```