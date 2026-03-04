from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from datetime import datetime
from pathlib import Path

from models.database import get_db, AudioRecording, Detection

router = APIRouter()

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

@router.get("/generate/{recording_id}")
async def generate_report(recording_id: int, db: Session = Depends(get_db)):
    """Generate compliance report for a recording"""
    
    # Get recording
    recording = db.query(AudioRecording).filter(
        AudioRecording.id == recording_id
    ).first()
    
    if not recording:
        raise HTTPException(404, "Recording not found")
    
    # Get detections
    detections = db.query(Detection).filter(
        Detection.recording_id == recording_id
    ).order_by(Detection.confidence.desc()).all()
    
    # Generate PDF
    filename = f"compliance_report_{recording_id}_{datetime.now().strftime('%Y%m%d')}.pdf"
    filepath = REPORTS_DIR / filename
    
    doc = SimpleDocTemplate(str(filepath), pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title = Paragraph("Wildlife Compliance Report", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 0.2 * inch))
    
    # Recording info
    info_data = [
        ["Recording Information", ""],
        ["Filename:", recording.filename],
        ["Date:", recording.created_at.strftime("%Y-%m-%d %H:%M")],
        ["Duration:", f"{recording.duration:.2f} seconds"],
        ["Sample Rate:", f"{recording.sample_rate} Hz" if recording.sample_rate else "N/A"],
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.3 * inch))
    
    # Summary
    summary = Paragraph(f"<b>Summary:</b> {len(detections)} wildlife detections identified", 
                       styles['Normal'])
    story.append(summary)
    story.append(Spacer(1, 0.2 * inch))
    
    # Detections table
    if detections:
        det_data = [["Species", "Common Name", "Type", "Confidence", "Time (s)"]]
        
        for det in detections[:20]:  # Limit to top 20
            det_data.append([
                det.species_name,
                det.common_name,
                det.detection_type.capitalize(),
                f"{det.confidence:.2%}",
                f"{det.start_time:.2f}"
            ])
        
        det_table = Table(det_data, colWidths=[2*inch, 1.5*inch, 0.8*inch, 1*inch, 0.8*inch])
        det_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        story.append(det_table)
    
    doc.build(story)
    
    return FileResponse(
        filepath,
        media_type='application/pdf',
        filename=filename
    )
