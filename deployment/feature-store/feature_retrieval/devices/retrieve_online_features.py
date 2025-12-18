from pprint import pprint
import constants
from feast import FeatureStore

# Initialize the feature store
store = FeatureStore(repo_path=constants.REPO_PATH)
# Get serving data from feature store, we retrieve
# all features


feature_vector = store.get_online_features(
    features=[
        "device_stats_stream:feature_5",
        "device_stats_stream:feature_3"
    ],
    entity_rows=[
        {"device_id": 2},
    ],
).to_dict()

pprint(feature_vector)
