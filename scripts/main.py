import filter_and_update_db
import load_data
import settings

settings.init()

load_data.load_csv_file_to_es()
filter_and_update_db.update_proper_records()
