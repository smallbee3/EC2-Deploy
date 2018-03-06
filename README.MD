# EC2 Deploy project


AWS의 EC2 배포를 연습하는 프로젝트입니다.
`.screts`폴더내의 파일로 비밀 키를 관리힙니다.

DB로 PostSQL을 사용하며, 'local'환경에서는 'localhost'의 DB, 'dev'환경과 'production'환경세ㅓ

## requirements

- Python (3.6)
- PostgreSQL


## Installation

```
pip install -r requirements.txt
```


## Secrets

**`.secrets/base.json`**

```json
{
    "SECRET_KEY": "<Django settings SECRET_KEY value>"
}
```

**`.secrets/dev.json`**

> PostgreSQL(AWS RDS)을 사용한다.

```json
{
  "DATABASE": {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "<자신의 RDS주소. ex)instance-name.###.region.reds.amazonaws.com>",
        "PORT": "<Port number, dafault:5432>",
        "NAME": "<DB name>",
        "USER": "<DB username>",
        "PASSWORD": "<DB user Password>"
    }
  }
}
```
