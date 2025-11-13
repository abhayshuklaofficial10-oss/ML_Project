import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # ✅ Dynamically detect project root
            base_path = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(base_path, "..", ".."))

            # ✅ Use "artifacts" instead of "artifact" (consistent with other scripts)
            artifacts_dir = os.path.join(project_root, "artifacts")

            # ✅ Full absolute paths
            model_path = os.path.join(artifacts_dir, "model.pkl")
            preprocessor_path = os.path.join(artifacts_dir, "preprocessor.pkl")

            print("📁 Checking paths...")
            print(f"Model path: {model_path}")
            print(f"Preprocessor path: {preprocessor_path}")

            # ✅ Create folder if missing
            if not os.path.exists(artifacts_dir):
                raise FileNotFoundError(f"❌ Artifacts folder not found: {artifacts_dir}")

            # ✅ Validate existence
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"❌ Model file missing at: {model_path}")

            if not os.path.exists(preprocessor_path):
                raise FileNotFoundError(f"❌ Preprocessor file missing at: {preprocessor_path}")

            print("✅ Loading model and preprocessor...")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            print("✅ Successfully loaded.")

            # ✅ Transform and predict
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            print("✅ Prediction complete.")
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
        self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int
    ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            # ✅ CORRECT column names
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],  # <-- Fixed
                "parental level of education": [self.parental_level_of_education], # <-- Fixed
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course], # <-- Fixed
                "reading score": [self.reading_score], # <-- Fixed
                "writing score": [self.writing_score], # <-- Fixed
            }

            df = pd.DataFrame(custom_data_input_dict)
            print("✅ Data successfully converted to DataFrame.")
            return df

        except Exception as e:
            raise CustomException(e, sys)