def normalize_features(features):

    mapping = {
        "Gym in building": "Gym",
        "Balcony with city view": "Balcony",
        "Dedicated home office": "Home Office",
        "Pet friendly property": "Pet Friendly",
    }

    normalized = []

    for feature in features:
        normalized.append(
            mapping.get(feature, feature)
        )

    return normalized