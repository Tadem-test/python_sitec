class SitecDataset:
    _akz = []
    _label = []
    _minima = []
    _maxima = []
    _latestTimestamp = []

    def get_akz(self):
        return self._akz

    def set_akz(self, akz):
        self._akz.append(akz)

    def get_label(self):
        return self._label

    def set_label(self, label):
        self._label.append(label)

    def get_minima(self):
        return self._minima

    def set_minima(self, minima):
        self._minima.append(minima)

    def get_maxima(self):
        return self._maxima

    def set_maxima(self, maxima):
        self._maxima.append(maxima)

    def get_latestTimestamp(self):
        return self._latestTimestamp

    def set_latestTimeStamp(self, latestimetamp):
        self._latestTimestamp.append(latestimetamp)

    def appendData(self, akz, label, minima, maxima, latestimetamp):
        self.set_akz(akz)
        self.set_label(label)
        self.set_minima(minima)
        self.set_maxima(maxima)
        self.set_latestTimeStamp(latestimetamp)

    def updateTimestampByIndex(self,position, datum):
        self._latestTimestamp[position] = datum
