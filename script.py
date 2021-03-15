import biketrauma_nmd

df = biketrauma_nmd.Load_db().save_as_df()
biketrauma_nmd.plot_location(biketrauma_nmd.get_accident(df))