# Learning How to Learn
## A single page webpage

### Description

I created a single page website from a brief. I followed the specifications closely. The webpage is about the learning process and it has 11 sections total, including the header and footer. This project was a continuation of a project I worked on in the past. The previous project was a static webpage, but I made some upgrades that made this iteration more dynamic. One of these upgrades include animations.

### Functionality

The links with icons, as well as the images in the Resources section lead to their corresponding pages. The other links on the page don't lead to other webpages yet, as the website is still being built.

### Technologies and Techniques

All links on the page change opacity when you hover over them with your mouse. I also inlcuded images and links to other websites with clickable icons.

#### Example:

'''
                    <a class="footer__link link_hover" href="https://facebook.com">
                      <img
                       class="footer__social-icon"
                       src="./images/facebook_color_white.svg"
                       alt="facebook">
                      Facebook
                    </a>
'''

I also used @keyframes to create rotating background images.

#### Example:


'''
@keyframes rotation {
  from {
    transform: rotate(0deg)
  }
  to {
    transform: rotate(360deg)
  }

}
'''
