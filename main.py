from social.app import App
from social.social_network import SocialNetwork
from social.clock import Clock


def main():
    clock = Clock()
    network = SocialNetwork(clock)
    app = App(network, clock)
    app.run()


if __name__ == "__main__":
    main()
