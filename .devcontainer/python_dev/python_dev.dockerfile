# .devcontainer/Dockerfile
ARG VERSION=latest
ARG IMAGE=python

FROM ${IMAGE}:${VERSION}

# Install git
RUN apt-get update && apt-get install -y git

# Install Python tools
COPY python/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install Oh My Zsh
RUN bash -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Autocompletion for bash, git, etc (it is customizable)
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"

# Create a non-root user
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
