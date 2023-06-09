# flipper-zero-in-stock-yet

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/technoguyfication/flipper-zero-in-stock-yet/docker-publish.yml)

## Description

This is a simple script that checks if Flipper Zero is in stock yet and sends a notification via the Twilio API to a list of phone numbers if it is.

If I find out this script is being used for scalping, I swear to god I will shove my foot so far up your ass you won't be able to breathe anymore.

## Getting Started

### Docker / Docker Compose (Recommended)

docker-compose.yml:

```yaml
version: '3'

services:
  fzisy:
    image: ghcr.io/technoguyfication/fzisy:main
    container_name: fzisy
    restart: unless-stopped

    environment:
      TWILIO_ACCOUNT_SID: "Your account SID"
      TWILIO_AUTH_TOKEN: "Your auth token"
      TWILIO_FROM_NUMBER: "Your Twilio number"
      SMS_BROADCAST_LIST: "+15558675309,+15558675310"
```
        
Docker Standalone:

```bash
docker run -d --name fzisy \
-e TWILIO_ACCOUNT_SID="Your account SID" \
-e TWILIO_AUTH_TOKEN="Your auth token" \
-e TWILIO_FROM_NUMBER="Your Twilio number" \
-e SMS_BROADCAST_LIST="+15558675309,+15558675310" \
ghcr.io/technoguyfication/fzisy:main
```

### Running Manually

Clone the project to a location of your choice and run these commands to install dependencies and run the script:

Running inside a [venv](https://docs.python.org/3/library/venv.html) is **highly** recommended.

```bash
pip install .
python3 -m fzisy
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [Flipper Zero](https://flipperzero.one/)
