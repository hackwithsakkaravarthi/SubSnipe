class DataSourceBase:
    def enumerate(self):
        raise NotImplementedError("Each data source must implement an enumerate method")
