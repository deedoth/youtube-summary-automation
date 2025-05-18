# FROM n8nio/n8n

# USER root

# # Install dependencies using Alpine's apk package manager
# RUN apk update && \
#     apk add --no-cache python3 py3-pip ffmpeg && \
#     pip3 install yt-dlp

# USER node


FROM n8nio/n8n

USER root

# Install dependencies
RUN apk update && \
    apk add --no-cache python3 py3-pip py3-virtualenv ffmpeg && \
    python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip install yt-dlp && \
    deactivate
