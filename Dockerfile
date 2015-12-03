FROM ubuntu:14.04
RUN apt-get update && apt-get install -y python-dev python-pip build-essential git wkhtmltopdf xorg
RUN echo -e '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf $*' > /usr/bin/wkhtmltopdf.sh
RUN chmod a+x /usr/bin/wkhtmltopdf.sh
RUN ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf
ADD . /app
ADD ./config /config
WORKDIR /app
RUN pip install -r requirements.txt
