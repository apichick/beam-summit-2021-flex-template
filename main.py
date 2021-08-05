import argparse
from pipeline.tweettrends import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tweets_topic",
        help="Input Cloud Pub/Sub topic"
        "projects/PROJECT/topics/TOPIC",
    )
    parser.add_argument(
        "--trends_topic",
        help="Output Cloud Pub/Sub topic"
        "projects/PROJECT/topics/TOPIC",
    )
    args, beam_args = parser.parse_known_args()

    run(
        tweets_topic=args.tweets_topic,
        trends_topic=args.trends_topic,
        beam_args=beam_args,
    )
