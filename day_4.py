
from datetime import datetime
import numpy as np

Class obse


def main():
    input_file = open('input/day_4_input.txt', 'r')
    observations = input_file.readlines()

    stamped_obvs = np.empty(len(observations))
    for observation in observations:
        parsed_obs = parse_observation(observation)
        np.append(stamped_obvs, [(parsed_obs)])


    for obvs in stamped_obvs:
        print(obvs)


def parse_observation(obs):

    time_stamp_str = obs.split('[', 1)[1].split(']')[0]
    time_stamp = datetime.strptime(time_stamp_str, '%Y-%m-%d  %H:%M')
    comment = obs.split(']')[1]

    return comment


if __name__ == "__main__":
    main()
