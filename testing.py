import os
from datetime import datetime
from model_prompting.model import Model

if __name__ == "__main__":
    model = Model()
    print(model.query())
