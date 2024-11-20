import os
import pandas as pd
import json


class JSONConverter:
    def json_to_dataframe(self, json_dir):
        """
        Reads a directory of JSON files and returns a DataFrame where each row is a JSON file.
        :param json_dir: Directory containing JSON files.
        :return: DataFrame with JSON data.
        """
        if not os.path.isdir(json_dir):
            raise ValueError(f"{json_dir} is not a valid directory.")
        
        data = []
        for filename in os.listdir(json_dir):
            filepath = os.path.join(json_dir, filename)
            if filename.endswith('.json') and os.path.isfile(filepath):
                with open(filepath, 'r') as f:
                    try:
                        data.append(json.load(f))
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON file {filename}: {e}")
        
        return pd.DataFrame(data)

    def dataframe_to_json(self, df, output_dir):
        """
        Writes a DataFrame to a directory, saving each row as a JSON file.
        :param df: DataFrame to be written to JSON files.
        :param output_dir: Directory where JSON files will be saved.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for index, row in df.iterrows():
            file_path = os.path.join(output_dir, f"row_{index}.json")
            with open(file_path, 'w') as f:
                json.dump(row.to_dict(), f, indent=4)
