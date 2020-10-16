# Ansible-Role for mautrix-telegram

The following variables **have to be set** (here with example values):
```yaml
mautrix_telegram_homeserver_domain: "labcode.de"
mautrix_telegram_as_token: "foo"
mautrix_telegram_hs_token: "bar"
mautrix_telegram_api_id: "2342"
mautrix_telegram_api_hash: "baz"
mautrix_telegram_permissions:
  "example.com": "admin"
```