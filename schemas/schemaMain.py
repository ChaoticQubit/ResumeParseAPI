from pydantic import BaseModel
from typing import List, Optional
from schemas.utilSchemas import *

class ApplicantName(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    title: str

class ApplicantPhone(BaseModel):
    phone: List[Optional[str]] = []

class ApplicantEmail(BaseModel):
    email: List[Optional[str]] = []

class ApplicantWebsite(BaseModel):
    website: List[Optional[str]] = []

class ApplicantLocation(Location):
    zipcode: str
    street: str
    street_number: str
    apartment: str

class ApplicantLanguages(BaseModel):
    languages: List[Optional[str]] = []

class ApplicantSummary(BaseModel):
    objective: str
    summary: str

class ApplicantEducation(BaseModel):
    education: List[Optional[Education]] = []

class ApplicantWorkExperience(BaseModel):
    total_work_experience: int
    work_experiences: List[Optional[WorkExp]] = []

class ApplicantSkills(BaseModel):
    skills: List[Optional[str]] = []

class ApplicantCertifications(BaseModel):
    certifications: List[Optional[str]] = []

class ApplicantAwards(BaseModel):
    awards: Optional[str] = None

class ApplicantPublications(BaseModel):
    publications: List[Optional[str]] = []

class ApplicantReferences(BaseModel):
    references: List[Optional[Reference]] = []

class ApplicantProjects(BaseModel):
    projects: str

class ApplicantExtracurriculars(BaseModel):
    extracurriculars: str

class GetFile(BaseModel):
    file_location: str
    file_name: str