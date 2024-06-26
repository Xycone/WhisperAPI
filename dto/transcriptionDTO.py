from pydantic import BaseModel
from model.modelSizes import ModelSizes

class TranscriptionDTO(BaseModel):
    model_size: ModelSizes
    diarisation: bool
    num_speakers: int
