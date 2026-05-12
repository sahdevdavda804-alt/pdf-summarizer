from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(summary_dict):

    path = "outputs/summary.pdf"

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    elements = []

    for heading, bullets in summary_dict.items():

        elements.append(
            Paragraph(
                f"<b>{heading}</b>",
                styles['Heading2']
            )
        )

        elements.append(Spacer(1, 10))

        for bullet in bullets:

            elements.append(
                Paragraph(
                    f"• {bullet}",
                    styles['BodyText']
                )
            )

            elements.append(Spacer(1, 5))

        elements.append(Spacer(1, 20))

    doc.build(elements)

    return path