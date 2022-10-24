class Playlists:
    def __init__(self, name, description, modifiedAt, numFollowers, numTracks, collaborative):
        self.name = name
        self.description = description
        self.modifiedAt = modifiedAt
        self.numFollowers = numFollowers
        self.numTracks = numTracks
        self.collaborative = collaborative


class Tracks:
    def __init__(self, name, durationMs):
        self.name = name
        self.durationMs = durationMs

class Albums:
    def __init__(self, name):
        self.name = name
        #self.artistId = artistId

class Artists:
    def __init__(self, name):
        self.name = name
