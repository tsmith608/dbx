from app.services.source_service import clean_source_line

# A typical "Dirty" RPG line found on a mainframe
dirty_line = "000100230501C     * This is a comment"

print(f"Original: [{dirty_line}]")
print(f"Cleaned:  [{clean_source_line(dirty_line)}]")

# Expected output: "C     * This is a comment"
