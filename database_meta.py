class DatabaseMeta(type): # this is a meta class
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:  # if there´s no instance, create a new instance.
            cls._instance = super().__call__(*args, **kwargs)
            return cls._instance

        return cls._instance  # if the instance already exist, return the instance.
