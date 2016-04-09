# Docker
----------------------------------------

## build

    # kumpel
    cd <Dockerfile/location>
    docker build --tag="kumpel" .

    # kumpel-redis
    docker run --name kumpel-redis -d redis -p 6379:6379 redis-server --appendonly yes

    # kumpel-mongodb
    docker run --name kumpel-mongo -d mongo -p 27017:27017

## docker-compose

### install

    curl -L https://github.com/docker/compose/releases/download/1.2.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

### use

    cd <docker-compose.yml/location>
    docker-compose up


WordPress on Docker (and HHVM/Nginx) Base
=========================================

## Things you may have to change

If you look at `/webroot/wp-config.php` you'll see that the setup has been adjusted to run with WordPress
in a subdirectory, and to take most config values you'd potentially have to change
from environment variables.

* In `docker-compose.yml`
  * Change the ports if you're running multiple versions of this setup
  * Change SITE_URL to your docker host (if it's not localhost)
* In `webroot/wp-config.php`:
  * Replace the salt section

## Handy Things

* `/tools/replace-db.sh`: replace the variables and use it to pull a copy of
your production database. To run the script in a container:

    % docker-compose -f docker-tools.yml run tools sh replace-db.sh

* `/tools/sync-assets.sh`: If you keep your production upload folder on disk and would like to mirror it to your local site, replace the variables in that file, and then:

    % docker-compose -f docker-tools.yml run tools sh sync-assets.sh [YOUR SFTP USERNAME]

* WP-CLI is installed and ready to run via `docker exec` in another terminal window while the site is running (under `docker-compose up`). First you'll need to find the ID of the running instance with `docker ps`. Copy that ID and you'll be able to run the cli like so:

    % docker exec [RUNNING ID] wp --allow-root --path=/srv/www/wp

  It's a handy way to update your plugins (amongst other things!).

* The [Memcached-Redux](https://wordpress.org/plugins/memcached-redux/) and [Redis Object Cache](https://wordpress.org/plugins/redis-cache/) plugins have been installed. To enable either, uncomment the appropriate sections (don't forget the links under web) in the `docker-compose.yml` file and copy the `object-cache.php` file from that plugin's folder to the `/webroot/content/` folder.

* The [Amazon S3 and CloudFront](https://wordpress.org/plugins/amazon-s3-and-cloudfront/) plugin and the [Amazon Web Services](https://wordpress.org/plugins/amazon-web-services/) plugin it depends on have been installed. I would highly recommend this if you're doing to run WordPress in a container. It will remove your dependency on volumes or shared storage if you run multiple instances of your site.

* WordPress is setup as a submodule, and I'll try to keep this repo pinned
to the latest version. Having said that, the first time you check this out, you'll need to run:

      % git submodule init
      % git submodule update

  If you need to update it yourself, go into the `/webroot/wp/` folder and run:

      % git fetch --tags
      % git checkout [VERSION NUMBER]

  Don't forget to commit your change in the main repo.




## Development

The webroot folder is mapped into the running vm in the docker-compose.yml (previously known as fig) setup. To start run:

    % docker-compose up

And you'll find your site at `http://[your docker host]:8000`

## Production

There is a starting point `docker-production.yml` file in the project root. It's tough to know exactly how you'll run in production, but assuming you've got dedicated DB and caching boxes, you'll just need to uncomment the appropriate lines. The HHVM we base this on is already tuned to run well behind load balancers, with things like the real ip module, and appropriate relaying of HTTPS status to HHVM.
