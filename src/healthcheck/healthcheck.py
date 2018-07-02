import logging
import time
import sys
import subprocess
import click
import notifier

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def retry_healthcheck(target, proxy, retries, retry_interval_seconds):
    for retry in range(retries):
        logging.info("Healthcheck try %s", retry)
        if healthcheck(target, proxy):
            logging.info("SUCCESS!")
            return
        logging.info("Call to %s via %s failed, retrying in %s seconds" %
                     (target, proxy, retry_interval_seconds))
        time.sleep(retry_interval_seconds)

    msg = "Failed to connect to %s" % target
    logging.warning(msg)
    notifier.alert(msg)


def healthcheck(target, proxy=None):
    try:
        subprocess.check_output(["curl", target, "-x", proxy, "-vv"])
        return True
    except subprocess.CalledProcessError as e:
        logging.error("Failed to execute request:\n{}".format(e.output))
    except Exception as e:
        logging.error("Unexpected error: {}".format(repr(e)))
    return False


@click.command()
@click.option('--target',
              help='target endpoint to do health check, i.e https://www.google.com',
              envvar='TARGET')
@click.option('--proxy',
              help='proxy endpoint (optional), i.e. https://<user>:<password>@some.proxy.com:8080',
              envvar='PROXY')
@click.option('--retries',
              default=3,
              help='number of retries',
              envvar='RETRIES')
@click.option('--interval-seconds',
              default=60,
              help='interval between checks',
              envvar='INTERVAL_SECONDS')
@click.option('--retry-interval-seconds',
              default=5,
              help='interval between retries in seconds',
              envvar='RETRY_INTERVAL_SECONDS')
def main(target, proxy, retries, interval_seconds, retry_interval_seconds):
    while True:
        retry_healthcheck(target, proxy, retries, retry_interval_seconds)
        logging.info("next health check in %s seconds", interval_seconds)
        time.sleep(interval_seconds)


if __name__ == '__main__':
    main()
