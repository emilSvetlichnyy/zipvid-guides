"""Zipvid pages. Facts come from the sources listed per page (seen in Google results on 2026-11-23)."""

APPLE_COMPRESS = ("Apple Support: Compress a video on iPhone", "https://support.apple.com/127765")
APPLE_HEVC = ("Apple Support: Using HEIF or HEVC media on Apple devices", "https://support.apple.com/116944")
DROPBOX_EMAIL = ("Dropbox: Send large videos over email", "https://www.dropbox.com/en_GB/resources/send-large-videos-over-email")
MOVAVI_WA = ("Movavi: How to compress videos for WhatsApp", "https://www.movavi.com/support/how-to/compress-video-for-whatsapp.html")
TELLA_DISCORD = ("Tella: Compress videos for Discord and email", "https://www.tella.com/help/tips/compress-videos-for-discord-and-email")
ADOBE_CODEC = ("Adobe: H.264 vs H.265 explained", "https://www.adobe.com/uk/creativecloud/file-types/video/codec/h264-vs-h265.html")

PAGES = []


def add(**kw):
    PAGES.append(kw)


add(
    slug="compress-video-iphone",
    group="compress",
    title="How to Compress a Video on iPhone (Free Options Compared)",
    description="Compress a video on iPhone: lower the resolution, use HEVC, or use a compressor app. What each way changes, with Apple's own size estimates.",
    h1="How to compress a video on iPhone",
    lead="Three ways to make a video file smaller on iPhone, and what each one costs in quality.",
    answer="A video gets smaller when you lower its <strong>resolution</strong>, its <strong>frame rate or bitrate</strong>, or re-encode it with <strong>HEVC</strong>. Apple's own way is exporting at a lower resolution in iMovie; a compressor app such as Zipvid does it in one step on the iPhone. Any compression can lower visual quality, so check the result before you delete the original.",
    steps=[
        "Decide where the video is going (messenger, email, storage). That sets the size you need.",
        "Pick a method: iMovie export at lower resolution, a compressor app, or shoot smaller next time (Settings → Camera).",
        "Compress a copy, not the original. Keep the original until you have watched the result.",
        "Watch the smaller file on your iPhone and check sound, sharpness and length.",
        "Delete the original only if you are happy, and empty Recently Deleted if you want the space back now.",
    ],
    body="""<h2>Apple's size estimates for one minute of video</h2>
<p>Apple lists these rough iMovie export sizes for one minute of footage shot with default iPhone settings:</p>
<table><thead><tr><th>Export resolution</th><th>Approx. size per minute</th></tr></thead><tbody>
<tr><td>1080p (default)</td><td>70–105 MB</td></tr>
<tr><td>720p</td><td>19–27 MB</td></tr>
<tr><td>540p</td><td>12–16 MB</td></tr>
<tr><td>360p</td><td>6–9 MB</td></tr>
</tbody></table>
<p class="meta">Source: Apple Support, "Compress a video on iPhone". Your numbers depend on the clip.</p>
<h2>Ways to compress, compared</h2>
<table><thead><tr><th>Method</th><th>Good for</th><th>Watch out for</th></tr></thead><tbody>
<tr><td>iMovie export at lower resolution</td><td>One video, Apple-made, no extra app</td><td>Several taps per video, no target size</td></tr>
<tr><td>Compressor app</td><td>Many videos, a target size, a fixed workflow</td><td>Check that it works on the device and does not upload your video</td></tr>
<tr><td>Change Camera settings</td><td>Smaller files from now on</td><td>Does not shrink videos you already have</td></tr>
</tbody></table>
<p>Related: <a href="../../share/compress-video-for-whatsapp/">fit a video under WhatsApp's limit</a>, <a href="../../formats/hevc-vs-h264-iphone/">HEVC vs H.264</a>.</p>""",
    cta="Pick one or more videos from your library, check the estimated result, choose HEVC or the widely compatible H.264, and save the smaller copy back. Everything runs on your iPhone, nothing is uploaded.",
    faqs=[
        ("Can I compress a video without losing any quality?", "Not completely. Apple notes that quality might be reduced when you lower the export resolution, and a smaller file means less data. A higher bitrate or HEVC keeps more detail for the same size, but it is still a trade-off."),
        ("Does compressing a video delete the original?", "No, as long as you save a copy. Keep the original until you have checked the smaller file."),
        ("Is it safe to use a compressor app?", "Check where processing happens. Zipvid compresses on the device and does not upload your videos."),
    ],
    sources=[APPLE_COMPRESS, APPLE_HEVC, ADOBE_CODEC],
    related=["compress-video-for-whatsapp", "hevc-vs-h264-iphone", "iphone-video-storage"],
)

add(
    slug="compress-video-for-whatsapp",
    group="share",
    title="Compress a Video for WhatsApp on iPhone (16 MB Limit)",
    description="WhatsApp sends videos up to about 16 MB directly. How to shrink a video under that limit on iPhone, and what to do if it still does not fit.",
    h1="How to compress a video for WhatsApp on iPhone",
    lead="WhatsApp's direct video limit is about 16 MB. Here is how to get under it.",
    answer="Sources agree that WhatsApp's limit for sending a video directly is about <strong>16 MB</strong>. Compress the video to a target under 16 MB (shorter, lower resolution, or both), or send it as a document, which has a much higher limit but arrives uncompressed. Limits can change, so check WhatsApp's own help if a send fails.",
    steps=[
        "Check the size: Photos → open the video → swipe up, or look in Files.",
        "If it is over 16 MB, compress a copy to a target below 16 MB. Aim a little lower, for example 14 to 15 MB, so it clearly fits.",
        "If it is too long for that size at good quality, trim it first or split it into parts.",
        "Send the smaller copy in WhatsApp. If you need the original quality, send it as a document instead.",
    ],
    body="""<h2>Which option when</h2>
<table><thead><tr><th>Situation</th><th>What to do</th></tr></thead><tbody>
<tr><td>Short clip, a bit over 16 MB</td><td>Compress to a 16 MB target</td></tr>
<tr><td>Long video</td><td>Trim or split first, then compress each part</td></tr>
<tr><td>Need the original quality</td><td>Send as a document (higher limit, no compression)</td></tr>
</tbody></table>
<p>Related: <a href="../compress-video-for-discord/">Discord limit</a>, <a href="../send-large-video-email-iphone/">email limit</a>.</p>""",
    img=("zipvid-messenger-presets", "Zipvid quality screen with a messenger preset set to WhatsApp 16 MB, resolution and format options", "Zipvid quality screen (sample data): messenger presets are part of Zipvid Pro."),
    cta="Zipvid Pro has a 16 MB size preset made for this: it targets the WhatsApp-style limit so you do not have to guess settings. Results depend on the video, and a long clip may need trimming first.",
    faqs=[
        ("What is the WhatsApp video size limit?", "Sources say about 16 MB when you send a video directly. Documents allow far larger files, but they are not re-encoded."),
        ("Why does my video look worse after WhatsApp?", "WhatsApp re-encodes videos to make them smaller. Sending it as a document avoids that."),
    ],
    sources=[MOVAVI_WA, APPLE_COMPRESS],
    related=["compress-video-iphone", "compress-video-for-discord", "send-large-video-email-iphone"],
)

add(
    slug="compress-video-for-discord",
    group="share",
    title="Compress a Video for Discord on iPhone (10 MB Target)",
    description="Discord's upload limit depends on your plan and has changed over time. A safe 10 MB target, and how to compress a video to it on iPhone.",
    h1="How to compress a video for Discord on iPhone",
    lead="The Discord limit depends on your plan. Compress to about 10 MB and it works almost everywhere.",
    answer="Discord's file limit depends on the sender's plan, and guides disagree on the exact numbers (they quote 8 MB or 10 MB for free accounts and more for Nitro). A <strong>10 MB target</strong> is the safe choice for most servers; check Discord's own help for the current limit.",
    steps=[
        "Check your plan and the current Discord limit.",
        "Compress a copy of the video to a target a little under the limit.",
        "Trim the clip to the part that matters. Short clips keep better quality at a small size.",
        "Upload the smaller copy in Discord and check that it plays.",
    ],
    body="""<p>Related: <a href="../compress-video-for-whatsapp/">WhatsApp limit</a>, <a href="../send-large-video-email-iphone/">email limit</a>.</p>""",
    cta="Zipvid Pro includes a 10 MB size preset. Pick the video, choose the preset and save the smaller copy. It runs on your iPhone. A long or very detailed clip may still need trimming to look good at 10 MB.",
    faqs=[
        ("What is the Discord video size limit?", "It depends on the plan and has changed over time. Guides quote 8 MB or 10 MB for free accounts and higher limits with Nitro, so verify it in Discord before you rely on a number."),
        ("How do I get a video under 10 MB?", "Shorten it, lower the resolution, and compress to a 10 MB target."),
    ],
    sources=[TELLA_DISCORD, APPLE_COMPRESS],
    related=["compress-video-for-whatsapp", "send-large-video-email-iphone", "compress-video-iphone"],
)

add(
    slug="send-large-video-email-iphone",
    group="share",
    title="How to Send a Large Video by Email From iPhone",
    description="Email attachment limits are around 20 to 25 MB. Ways to send a large video from iPhone: Mail Drop, cloud link, AirDrop, or compress it first.",
    h1="How to send a large video by email from iPhone",
    lead="Most email services cap attachments near 25 MB. Here are the ways around it.",
    answer="Gmail, Yahoo Mail and ProtonMail allow about <strong>25 MB</strong>, while Outlook and iCloud Mail allow about <strong>20 MB</strong>. To send more, use <strong>Mail Drop</strong> (a link instead of an attachment), a cloud link, or AirDrop. Or compress the video under the limit and attach it.",
    steps=[
        "Check the video size and the limit of the recipient's mail service.",
        "Small overshoot: compress a copy to under 20 MB (safe for most providers) and attach it.",
        "Large video: use Mail Drop, or upload to Google Drive, Dropbox or OneDrive and paste the link.",
        "Nearby Apple device: AirDrop has no fixed size limit, but very large files can fail or be slow.",
    ],
    body="""<h2>Limits at a glance</h2>
<table><thead><tr><th>Service</th><th>Attachment limit</th></tr></thead><tbody>
<tr><td>Gmail, Yahoo Mail, ProtonMail</td><td>25 MB</td></tr>
<tr><td>Outlook, iCloud Mail</td><td>20 MB</td></tr>
</tbody></table>
<p class="meta">Source: Dropbox's list. Providers can change limits.</p>
<p>Related: <a href="../compress-video-for-whatsapp/">WhatsApp limit</a>, <a href="../../compress/compress-video-iphone/">compress a video on iPhone</a>.</p>""",
    cta="Zipvid Pro includes a 20 MB size preset, a safe target for Outlook and iCloud Mail and below Gmail's limit. The smaller copy is saved to your library, ready to attach.",
    faqs=[
        ("Why does my email say the attachment is too large?", "Most providers limit attachments to around 20 to 25 MB, and encoding makes the real message a bit bigger than the file."),
        ("Does compressing a video before emailing hurt quality?", "It can. Aim for the smallest reduction that fits, and compare the result with the original."),
    ],
    sources=[DROPBOX_EMAIL, APPLE_COMPRESS],
    related=["compress-video-for-whatsapp", "compress-video-for-discord", "compress-video-iphone"],
)

add(
    slug="hevc-vs-h264-iphone",
    group="formats",
    title="HEVC vs H.264 on iPhone: Which to Choose?",
    description="High Efficiency (HEVC) usually makes smaller files; Most Compatible (H.264) plays almost everywhere. How to choose on iPhone, with sources.",
    h1="HEVC vs H.264 on iPhone: which one to choose",
    lead="One makes smaller files, the other plays almost everywhere.",
    answer="<strong>HEVC (H.265)</strong> usually makes files noticeably smaller than <strong>H.264</strong> at similar quality, but H.264 is the safer choice for sharing and for older devices. Use High Efficiency for storage, and Most Compatible (or an H.264 export) when you share outside the Apple world. Savings vary with the video.",
    steps=[
        "Open Settings → Camera → Formats.",
        "Choose <strong>High Efficiency</strong> for smaller files (HEVC).",
        "Choose <strong>Most Compatible</strong> for H.264 if you share often with older devices or non-Apple platforms.",
        "For an existing video, export or compress a copy in the format you need.",
    ],
    body="""<table><thead><tr><th></th><th>HEVC (H.265)</th><th>H.264</th></tr></thead><tbody>
<tr><td>File size</td><td>Usually smaller at similar quality</td><td>Larger</td></tr>
<tr><td>Compatibility</td><td>Newer devices and apps</td><td>Almost everything</td></tr>
<tr><td>Good for</td><td>Saving space</td><td>Sharing and uploads</td></tr>
</tbody></table>
<p>Apple notes that media can be converted to H.264 when you import it to a PC or share it with a device that does not support HEVC.</p>
<p>Related: <a href="../../compress/compress-video-iphone/">compress a video on iPhone</a>.</p>""",
    cta="Zipvid lets you compress with modern HEVC or widely compatible H.264. In Pro's manual mode you choose the resolution and the format yourself.",
    faqs=[
        ("Is HEVC the same as H.265?", "Yes. HEVC (High Efficiency Video Coding) is the same codec as H.265."),
        ("How much smaller is HEVC?", "Sources say about half the size in the best case and around 20 to 25% in one test. Savings depend on the video, so do not expect a fixed number."),
    ],
    sources=[APPLE_HEVC, ADOBE_CODEC],
    related=["compress-video-iphone", "iphone-video-storage"],
)

add(
    slug="iphone-video-storage",
    group="formats",
    title="Why Videos Take So Much Space on iPhone (and What to Do)",
    description="Why iPhone videos are so big, what changes the size, and how to cut it: resolution, frame rate, HDR and format. Based on Apple's own guidance.",
    h1="Why videos take so much space on iPhone",
    lead="What decides the size of a video, and the settings that make future videos smaller.",
    answer="Video size comes from resolution, frame rate, HDR and format. Apple suggests choosing a resolution below the default 1080p, turning off HDR Video, and making sure <strong>High Efficiency</strong> is selected to keep future files smaller. For videos you already have, compress a copy and delete the original.",
    steps=[
        "Settings → Camera → Record Video: choose a lower resolution than you need.",
        "Turn off HDR Video if you do not need it.",
        "Settings → Camera → Formats: choose High Efficiency.",
        "Compress big videos you already have, then delete the originals and empty Recently Deleted.",
    ],
    body="""<p>One guide also notes that 30 fps instead of 60 fps can cut file size noticeably with a small visible difference. Treat that as a rule of thumb.</p>
<p>Related: <a href="../hevc-vs-h264-iphone/">HEVC vs H.264</a>, <a href="../../compress/compress-video-iphone/">compress a video on iPhone</a>.</p>""",
    cta="Zipvid compresses the videos you already have, on the iPhone. See the estimate before you start, then save the smaller copy. Free covers 3 compressions, up to 2 videos at a time.",
    faqs=[
        ("Why is a one-minute video so large?", "At the default 1080p, Apple estimates roughly 70 to 105 MB per minute for iMovie exports; 4K and 60 fps are larger."),
        ("Will deleting the original free space immediately?", "Deleted items stay in Recently Deleted for 30 days. Empty that album to get the space back right away."),
    ],
    sources=[APPLE_COMPRESS, APPLE_HEVC],
    related=["hevc-vs-h264-iphone", "compress-video-iphone"],
)
