from PyLeague.base_challenge import BaseChallenge, BaseTest, BaseWeights


class FrameCountWeights(BaseWeights):
    def calculate_time(self, time):
        # Make the time more relevant. Lowers the usefulness of a regex.
        return super(FrameCountWeights, self).calculate_time(time) * 100


class FrameCountChallenge(BaseChallenge):
    TESTS = [
        BaseTest(["abc_def[10-100].jpg"], 91),
        BaseTest(["abc_def[10-100]"], 91),
        BaseTest(["[10-100]abc_def"], 91),
        BaseTest(["[-]abc_def"], 0),
        BaseTest(["abc_def"], 0),
        BaseTest(["[10-100]abc_def[20-200]"], 181),
        BaseTest(["[10-100]abc[3-4]_def[20-200]"], 181),
        BaseTest(["[10-100.0]abc[3.2-4]_def[20_200]"], 0),
        BaseTest(["SCC1680_comp_v084_z003_left.[1001-1023].exr"], 23),
        BaseTest(["SCC1680_comp_[1001_345-45]_v084_z003_left.[1001-1023].exr"], 23),
        BaseTest(["foo[1001-1023]/SCC1680_comp_[1001_345-45]_v084_z003_left.[1001-1015].exr"], 15),
        BaseTest(["foo[1001_345-45]_v084_z003_left.[5].exr"], 0),
    ]
    user_function_name = "frames"

    def __init__(self):
        super(FrameCountChallenge, self).__init__(weights=FrameCountWeights())


challenge_1 = FrameCountChallenge()
