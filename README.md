# Dynami - DynDNS Update Client

## Installation

### Python Module

```shell
pip install --user dynami
```

### Quick installation

```shell
curl -sSL https://ext.bytesentinel.io/dynami/install.sh | bash
```

### Manual installation

```shell
COMING SOON
```

## Provider

- [x] Hetzner
- [ ] Cloudflare
- [ ] Azure
- [ ] STRATO
- [ ] IONOS
- [ ] GoDaddy
- [ ] AWS

## Examples

### Hetzner

```python
from dynami.provider import Hetzner
from dynami.ext import Client

provider = Hetzner(api_key="abcdefghijklmnopqrstuvwxyz", zone="bytesentinel.io", record="dyn")
client = Client(provider=provider)
update = client.update("8.8.8.8")
if update.status_code == 200:
    print("Updated!")
else:
    print("Failed!")
```