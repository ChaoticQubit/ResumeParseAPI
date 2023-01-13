from pydantic import BaseModel

class Accreditation(BaseModel):
    degree: str
    education_level: str
    original_str: str

class Grade(BaseModel):
    metric: str
    value: str

class Location(BaseModel):
    city: str
    state: str
    country: str

class Dates(BaseModel):
    start_date: str
    end_date: str
    is_current: str

class MetaData(BaseModel):
    job_title: str
    management_level: str
    minor_group: str
    sub_major_group: str
    major_group: str
    group_title: str
    soc_code: str

class Education(BaseModel):
    organization: str
    accreditation: Accreditation
    grade: Grade
    location: Location
    dates: Dates

class WorkExp(BaseModel):
    title: str
    organization: str
    description: str
    dates: Dates
    location: Location
    metadata: MetaData

class Reference(BaseModel):
    name: str
    email: str
    phone: str
    text: str