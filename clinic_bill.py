from arabic import convert
from reportlab.lib.units import inch
def clinic_temp(c):
    c.setFillColor("red")
    c.setFont("Arabic",26)
    c.drawString(2.2*inch,7.8*inch,convert('الدكتور'))
    c.setFillColor("blue")
    c.setFont("Arabic",18)
    c.drawString(2.2*inch,7.2*inch,convert('علي فيصل'))
    c.setFillColor("black")
    c.setFont("Arabic",12)
    c.drawString(1.1*inch,6.8*inch,convert(' لامراض المفاصل و الروماتزم و الاعصاب و الفقرات'))
    c.setFillColor("black")
    c.setFont("Arabic",12)
    c.drawString(1*inch,6.4*inch,convert('و تاهيل اصابات الكسور و الحبل الشوكي و العلاج بالليزر'))
    c.setFillColor("blue")
    c.drawString(1.5*inch,6*inch,"MbChB Rheumatolgy & Rehabilitation")
    c.drawImage('images/knee.png',0.5*inch,7*inch)
    c.drawImage("images/aa.png",4.5*inch,7*inch)
    c.drawImage('images/b.png',4.4*inch,5.4*inch)
    c.setStrokeColor("blue")
    c.setLineWidth(1.2)
    c.line(0.8*inch,5.4*inch,5*inch,5.4*inch)
    c.setFillColor("black")
    c.setFont("Arabic",12)
    c.drawString(4.7*inch,5.1*inch,convert('اسم المريض :'))
    c.drawString(1*inch,5.1*inch,convert('التاريخ  :'))
    c.drawString(4.7*inch,4.8*inch,convert('العمر :'))
    c.drawString(1*inch,4.8*inch,convert('الجنس  :'))
    
    c.setFillColor("black")
    c.drawString(0.1*inch,4.4*inch,"Treatment :")
    c.setStrokeColor("blue")
    c.setLineWidth(1)
    c.line(0.1*inch,4.3*inch,1.4*inch,4.3*inch)
    
    c.setFillColor("red")
    c.setFont("Arabic",12)
    c.drawString(3.8*inch,0.5*inch,convert('رقم الحجز  07733349868'))
    c.drawString(3.35*inch,0.2*inch,convert('رقم التسجيل 40484 في 2010'))
    
    c.setFillColor("grey")
    c.setFont("Arabic",10)
    c.drawString(1.1*inch,0.5*inch,convert('العنوان - البصرة -القرنة'))
    c.drawString(0.1*inch,0.2*inch,convert('شارع الفردوس - مقابل خدمات عارف للتبريد'))
    c.rotate(35)
    c.setFillColorCMYK(0,0,0,0.1)
    c.setFont("Helvetica",60)
    c.drawString(1.5*inch,0.1*inch,"Dr. Ali's Clinic")
    c.rotate(-35)
    return c