# AI App

## Build image and push
```bash
sudo docker buildx build . --push --platform linux/arm64 -t <registry-ip-address>:32000/ai:latest
```

