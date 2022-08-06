# build wut
FROM wiiuenv/devkitppc:20220801 AS final

ENV openssl_ver=3.0.5 \
 curl_ver=7.84.0 \
 DEBIAN_FRONTEND=noninteractive \
 PATH=$DEVKITPPC/bin:$PATH \
 WUT_ROOT=$DEVKITPRO/wut
WORKDIR /

RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2 && \
 apt-get update && \
 apt-get -y --no-install-recommends upgrade && \
 apt-get -y install --no-install-recommends autoconf automake libtool openjdk-11-jre-headless && \
 apt-get clean && \
 rm -rf /var/lib/apt/lists/* /usr/share/man && \
 git clone --recursive https://github.com/wiiu-env/libmocha --single-branch && \
 cd libmocha && \
 git checkout b0dee4269875a62ea2a4b40e58dd919de07cdee2 && \
 make -j$(nproc) && \
 make install && \
 cd .. && \
 rm -rf libmocha && \
 mkdir /nuspacker && \
 cd /nuspacker && \
 wget https://github.com/Maschell/nuspacker/raw/master/NUSPacker.jar

WORKDIR /project
