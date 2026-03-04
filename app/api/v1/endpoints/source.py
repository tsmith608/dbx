from fastapi import APIRouter, HTTPException
from app.services.source_service import read_source_member

router = APIRouter()

@router.get("/{library}/{file}/{member}")
def get_source(library: str, file: str, member: str):
    #fetch and clean provided source member
    try:
        content = read_source_member(library, file, member)
        return {
            library,
            file,
            member,
            content
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")