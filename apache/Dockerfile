# Start with a Debian/Ubuntu-based image
FROM ubuntu:latest

# Update package list and install Apache
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

COPY ./httpd.conf /etc/apache2/sites-available/000-default.conf
    
# Enable required Apache modules
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN a2enmod proxy_balancer
RUN a2enmod lbmethod_byrequests


EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]