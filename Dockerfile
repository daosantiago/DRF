FROM ubuntu

# Instala pacotes básicos (wget, unzip etc.)
RUN apt-get update && apt-get install -y wget unzip default-jre \
    && rm -rf /var/lib/apt/lists/*

# Baixa e instala o Sencha Cmd
# RUN wget https://cdn.sencha.com/cmd/7.5.1/no-jre/SenchaCmd-7.5.1.20-linux-amd64.sh.zip -O /tmp/SenchaCmd.zip \
#     && unzip -o /tmp/SenchaCmd.zip -d /tmp \
#     && chmod +x /tmp/SenchaCmd-7.5.1.20-linux-amd64.sh \
#     && /tmp/SenchaCmd-7.5.1.20-linux-amd64.sh -q -dir /opt/Sencha -- -Dlicense.agreement=Y \
#     && ln -s /opt/Sencha/SenchaCmd-7.5.1.20/sencha /usr/local/bin/sencha \
#     && rm -rf /tmp/*

# Definir diretório de trabalho
WORKDIR /app

# Se quiser copiar seu projeto diretamente pra imagem (geralmente é melhor em pipelines fazer o checkout fora)
# COPY . /app

CMD ["/bin/bash"]