<div align="center">
    <img src="./.assets/bytesentinel.png" width="250px" style="margin-left: 10px" />
</div>

<h1 align="center">
  dynami
</h1>

<div align="center">
    <img src="https://img.shields.io/github/downloads/bytesentinel-io/dynami/total?style=for-the-badge" />
    <img src="https://img.shields.io/github/last-commit/bytesentinel-io/dynami?color=%231BCBF2&style=for-the-badge" />
    <img src="https://img.shields.io/github/issues/bytesentinel-io/dynami?style=for-the-badge" />
</div>

<br />

`dynami` is a Python package that provides a simple interface for managing DNS records through various providers. Currently, it supports Hetzner as a DNS provider, with more providers to come in future updates.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z8Z8JPE9P)

## Installation

You can install dynami via pip:

```shell
pip install dynami
```

## Usage

To use `dynami`, you must first instantiate a provider and client. Here's an example for Hetzner:

```python
from dynami.provider import Hetzner
from dynami.ext import Client

api_key = "YOUR_API_KEY"
zone = "yourdomain.local"

provider = Hetzner(api_key=api_key, zone=zone)
client = Client(provider)

result = client.set(record="www", type="A", value="0.0.0.0")

if result.status_code < 299 and result.status_code > 199:
    print("Success!")
else:
    print("Failed!")

```

This will create an A record for the www subdomain pointing to 0.0.0.0.

## Providers

Currently, `dynami` only supports Hetzner as a DNS provider. More providers will be added in future updates.

- [x] Hetzner
- [ ] Amazon Web Services (AWS)
- [ ] Cloudflare
- [ ] DigitalOcean
- [ ] Google Cloud Platform (GCP)
- [ ] Microsoft Azure

### Provider configuration

To configure a provider, pass the provider-specific options to its constructor. For Hetzner, these options are:

- `api_key`: your Hetzner DNS API key
- `zone`: the name of the DNS zone you want to manage

## Client methods

`Client` provides the following methods for managing DNS records:

- `set`: creates or updates a DNS record
