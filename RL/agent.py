class Agent:

    def __init__(self, state_space_size: int, action_space_size: int) -> None:
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.lr = 0.001
        self.y = 0.99
        self.model = None
        self.training = True
        self.step_count = 0
        self.episode_count = 0
        self.train_count = 0
        self.rewards = []
        self.reward_history = []

    def create_model(self, *args, **kwargs) -> None:
        pass

    def save_model(self, path) -> None:
        pass

    def load_model(self, path) -> None:
        pass

    def learn(self, *args, **kwargs) -> None:
        pass

    def policy(self, state, greedy=False):
        pass
