import csv

# Shot Data
class Shot:
    class Stroke: # Enum
        UNKNOWN = 0
        FEED = 1
        FOREHAND = 2
        BACKHAND = 3
        FOREHAND_VOLLEY = 4
        BACKHAND_VOLLEY = 5
        OVERHEAD = 6

        @staticmethod
        def string_to_enum(stroke):
            if stroke == 'Feed':
                return Shot.Stroke.FEED
            elif stroke == 'Forehand':
                return Shot.Stroke.FOREHAND
            elif stroke == 'Backhand':
                return Shot.Stroke.BACKHAND
            elif stroke == 'FH Volley':
                return Shot.Stroke.FOREHAND_VOLLEY
            elif stroke == 'BH Volley':
                return Shot.Stroke.BACKHAND_VOLLEY
            elif stroke == 'Overhead':
                return Shot.Stroke.OVERHEAD
            print 'What is this?', stroke
            return Shot.Stroke.UNKNOWN

        @staticmethod
        def enum_to_string(stroke):
            if stroke == Shot.Stroke.FEED:
                return 'Feed'
            elif stroke == Shot.Stroke.FOREHAND:
                return 'Forehand'
            elif stroke == Shot.Stroke.BACKHAND:
                return 'Backhand'
            elif stroke == Shot.Stroke.FOREHAND_VOLLEY:
                return 'FH Volley'
            elif stroke == Shot.Stroke.BACKHAND_VOLLEY:
                return 'BH Volley'
            elif stroke == Shot.Stroke.OVERHEAD:
                return 'Overhead'
            return 'Unknown'

    class Spin: # Enum
        UNKNOWN = 0
        FLAT = 1
        TOPSPIN = 2
        SLICE = 3

        @staticmethod
        def string_to_enum(spin):
            if spin == 'Flat':
                return Shot.Spin.FLAT
            elif spin == 'Topspin':
                return Shot.Spin.TOPSPIN
            elif spin == 'Slice':
                return Shot.Spin.SLICE
            print 'What is this?', stroke
            return Shot.Spin.UNKNOWN

        @staticmethod
        def enum_to_string(spin):
            if spin == Shot.Spin.FLAT:
                return 'Flat'
            elif spin == Shot.Spin.TOPSPIN:
                return 'Topspin'
            elif spin == Shot.Spin.SLICE:
                return 'Slice'
            return 'Unknown'

    mPlayer = ''
    mShotCount = -1
    mType = None # TODO: What is this?
    mStroke = None # Stroke Enum
    mSpin = None # Spin Enum
    mSpeed = 0.0
    # TODO: The rest of the info

    def __init__(self, player, shotCount, type, stroke, spin, speed):
        self.mPlayer = player
        self.mShotCount = shotCount
        self.mType = type
        self.mStroke = stroke
        self.mSpin = spin
        self.mSpeed = speed

    def print_string(self):
        print self.mPlayer, ',', self.mShotCount, ',', self.mType, ',', Shot.Stroke.enum_to_string(self.mStroke), ',', Shot.Spin.enum_to_string(self.mSpin), ',', self.mSpeed
