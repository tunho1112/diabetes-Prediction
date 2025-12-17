from feast import Entity

device = Entity(
    name="diabete",
    join_keys=["diabete_id"],
    description="diabete id",
)
