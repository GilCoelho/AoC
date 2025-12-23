# .devcontainer/Dockerfile
ARG VERSION=latest
ARG IMAGE=python

FROM ${IMAGE}:${VERSION}

# Install git
RUN apt-get update && apt-get install -y git

# Install Python tools
COPY python/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install zsh with autocompletion tools
RUN apt-get update && apt-get install -y \
    curl \
    zsh \
    zsh-autosuggestions \
    zsh-syntax-highlighting

# Create a non-root user
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME --shell /bin/zsh

# Install Oh My Zsh for better zsh experience
USER $USERNAME
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install powerlevel10k theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
