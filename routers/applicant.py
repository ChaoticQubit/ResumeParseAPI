from fastapi import APIRouter, FastAPI
import schemas.schemaMain as schemas
import json, utils

router = APIRouter(
    prefix="/applicant",
    tags=["Applicant"],
)

# sas_url = ""

# @router.post("/file")
# async def getFile(file: schemas.GetFile):
#     global sas_url
#     sas_url = utils.__generateSASTokenForBlob(filepath=file.file_location, filename=file.file_name)

# doc = utils.__getParsedAffindaData(sas_url)

@router.post("/all")
async def read_applicant(file: schemas.GetFile):
    sas_url = utils.__generateSASTokenForBlob(filepath=file.file_location, filename=file.file_name)
    doc = utils.__getParsedAffindaData(sas_url)
    return doc

# @router.get("/name", response_model=schemas.ApplicantName)
# def read_applicant_name():
#     return doc['name']

# @router.get("/phone", response_model=schemas.ApplicantPhone)
# def read_applicant_phone():
#     return {'phone': doc['phone']}

# @router.get("/email", response_model=schemas.ApplicantEmail)
# def read_applicant_email():
#     return {'email': doc['email']}

# @router.get("/website", response_model=schemas.ApplicantWebsite)
# def read_applicant_website():
#     return {'website': doc['website']}

# @router.get("/location", response_model=schemas.ApplicantLocation)
# def read_applicant_location():
#     return doc['location']

# @router.get("/langs", response_model=schemas.ApplicantLanguages)
# def read_applicant_prefered_languages():
#     return {'languages': doc['languages']}

# @router.get("/summary", response_model=schemas.ApplicantSummary)
# def read_applicant_summary():
#     sub_doc = doc['summary']
#     return {'objective': sub_doc['objective'], 'summary': sub_doc['summary']}

# @router.get("/education", response_model=schemas.ApplicantEducation)
# def read_applicant_education():
#     return {'education': doc['education']}

# @router.get("/workex", response_model=schemas.ApplicantWorkExperience)
# def read_applicant_work_experience():
#     sub_doc = doc['work_experience']
#     return {'total_work_experience': sub_doc['total_work_experience'], 'work_experiences': sub_doc['work_history']}

# @router.get("/skills", response_model=schemas.ApplicantSkills)
# def read_applicant_skills():
#     return {'skills': doc['skills']}

# @router.get("/certs", response_model=schemas.ApplicantCertifications)
# def read_applicant_certifications():
#     return {'certifications': doc['certifications']}

# @router.get("/awards", response_model=schemas.ApplicantAwards)
# def read_applicant_awards():
#     return {'awards': doc['awards']}

# @router.get("/publications", response_model=schemas.ApplicantPublications)
# def read_applicant_publications():
#     return {'publications': doc['publications']}

# @router.get("/references", response_model=schemas.ApplicantReferences)
# def read_applicant_references():
#     return {'references': doc['references']}

# @router.get("/projects", response_model=schemas.ApplicantProjects)
# def read_applicant_projects():
#     return {'projects': doc['projects']}

# @router.get("/extraco", response_model=schemas.ApplicantExtracurriculars)
# def read_applicant_extracurriculars():
#     return {'extracurriculars': doc['extracurriculars']}
