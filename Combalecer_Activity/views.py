from django.shortcuts import render
from django.http import HttpResponse

def ccms_mission(request):
    msg = """<h3>CCMS Mission</h3>
    <p>The College of Computing and Multimedia Studies shall produce technically competent Information Technology professionals adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence</p>"""

    return HttpResponse(msg)

def ccms_vision(request):
    msg = """<h3>CCMS Vision</h3>
    <p>The College of Computing and Multimedia Studies shall be a Center of Excellence in Information Technology education</p>"""

    return HttpResponse(msg)

def ccms_objectives(request):
    msg = """<h3>CCMS Program Educational Objectives</h3>
    <p>After graduation, alumni of MSEUF-CCMS programs shall:</p>
    <ol>
    <li>Be Employed and demonstrate professionalism, competence, and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions</li>
    <li>Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market; and</li>
    <li>Exhibit leadership, teamwork, and commitment to their respective local or global organizations</li>
    </ol>"""

    return HttpResponse(msg)

def opening(request):
    msg = """<h3>CSIPT Activity</h3>
    <p>URLs for this Activity are:</p>
    <ol>
    <li>admin/</li>
    <li>ccms_mission/</li>
    <li>ccms_vision/</li>
    <li>ccms_objectives/</li>
    </ol>
    
     <p>Thank you!</p>"""

    return HttpResponse(msg)