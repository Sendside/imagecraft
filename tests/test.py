

# Python standard library
import os

# This module
from imagecraft import ImageGenerator

FILE_EXT = "png"
FILE_FORMAT = "PNG"

RGB24_COLORS = {
    'red': '#FF0000',
    'yellow': '#FFFF00',
    'green': '#007700',
    'blue': '#0000AA',
    'orange': '#FF6600',
    'purple': '#9900BB',
    'white': '#FFFFFF',
    'black': '#000000',
    'transparent': None,
}

RGB12_COLORS = {
    'red': '#F00',
    'yellow': '#FF0',
    'green': '#070',
    'blue': '#00A',
    'orange': '#F60',
    'purple': '#90B',
    'white': '#FFF',
    'black': '#000',
    'transparent': None,
}

NAMED_COLORS = {
    'red': 'red',
    'yellow': 'yellow',
    'green': 'green',
    'blue': 'blue',
    'orange': 'orange',
    'purple': 'purple',
    'white': 'white',
    'black': 'black',
    'transparent': 'transparent',
}

RGBTUP_COLORS = {
    'red': (255,0,0),
    'yellow': (255,255,0),
    'green': (0,110,0),
    'blue': (0,0,220),
    'orange': (256,96,0),
    'purple': (164,00,204),
    'white': (255,255,255),
    'black': (0,0,0),
    'transparent': None,
}

class GeneratorTest(ImageGenerator):
    """ImageGenerator subclass for running tests."""
    _default_source_path = os.path.join(os.path.dirname(__file__), 'source')
    _default_output_path = os.path.join(os.path.dirname(__file__), 'output')
    image_format = FILE_FORMAT


class SingleGradientTest(GeneratorTest):
    """Creates a single image gradient. Should produce a square with solid
    red in the upper-left with a gradient toward transparent at the bottom
    right."""
    output_filename = "single_gradient_test.%s" % FILE_EXT
    layers = (
        {'white': 'rgba_grad_ne.png'},
    )


class DualGradientTest(GeneratorTest):
    """Overlays two differently-colored image gradients. Should produce a
    square with solid green at the upper left blending into solid red at the
    bottom right."""
    output_filename = "dual_gradient_test.%s" % FILE_EXT
    layers = (
        {'red': 'rgba_grad_ne.png'},
        {'white': 'rgba_grad_nw.png'},
    )


class QuadGradientTest(GeneratorTest):
    """Overlays two differently-colored image gradients. Should produce a
    square with white at the bottom right, blue at the bottom left,
    green at the top left and red at the top right. The center should be
    nearly transparent."""
    output_filename = "quad_gradient_test.%s" % FILE_EXT
    layers = (
        {'red': 'rgba_grad_ne.png'},
        {'green': 'rgba_grad_nw.png'},
        {'blue': 'rgba_grad_sw.png'},
        {'white': 'rgba_grad_se.png'},
    )


class SolidStarTest(GeneratorTest):
    """Creates a star over a solid background color. Should produce a yellow
    star over a red background."""
    output_filename = "solid_star_test.%s" % FILE_EXT
    layers = (
        {'red': 'rgb_solid.png'},
        {'yellow': 'rgba_star.png'},
    )


class AlphaStarTest(GeneratorTest):
    """Creates a star over an alpha-transparent gradient background. Should
    produce a purple star over a yellow-and-orange alpha-transparent background
    """
    output_filename = "alpha_star_test.%s" % FILE_EXT
    layers = (
        {'orange': 'rgba_grad_ne.png'},
        {'yellow': 'rgba_grad_se.png'},
        {'orange': 'rgba_grad_sw.png'},
        {'yellow': 'rgba_grad_nw.png'},
        {'purple': 'rgba_star.png'},
    )


class OriginalColorTest(GeneratorTest):
    """Superimposes an unmodified alpha-transparent RGB color wheel over a
    colored background. The colour wheel collours should be preserved (not
    colorized)."""
    output_filename = "original_color_test.%s" % FILE_EXT
    layers = (
        {'black': 'rgb_solid.png'},
        {'red': 'rgba_grad_ne.png'},
        {'green': 'rgba_grad_nw.png'},
        {'blue': 'rgba_grad_sw.png'},
        {'white': 'rgba_grad_se.png'},
        {'transparent': 'rgba_rgb_wheel.png'},
    )


class ComplexGradientTest(GeneratorTest):
    """Draws two gradients; one over a transparency and the other over a
    solid-colored box."""
    output_filename = "complex_gradient_test.%s" % FILE_EXT
    layers = (
        {'red': 'rgba_solid_top.png'},
        {'blue': 'rgba_gradalpha.png'},
        {'yellow': 'rgba_grad_star.png'},
    )


class GradientStripe(GeneratorTest):
    """Draws a couple gradients. This caused some problems previously because
    the black wouldn't render (matting issues). You should see white gradients
    at the top and (subtle) black gradients at the bottom."""
    output_filename = "gradient_stripe.%s" % FILE_EXT
    layers = (
        {'white': 'gradstripe_top.png'},
        {'black': 'gradstripe_bottom.png'},
    )


def main():
    """Runs some stupid tests"""
    global FILE_EXT
    global FILE_FORMAT
    FILE_EXT = 'png'
    FILE_FORMAT = 'PNG'

    c = RGB24_COLORS
    for test in (
            SingleGradientTest,
            DualGradientTest,
            QuadGradientTest,
            SolidStarTest,
            AlphaStarTest,
            OriginalColorTest,
            ComplexGradientTest,
            GradientStripe,
            ):
        test(c).render()

if __name__ == "__main__":
    # Executes all tests when called directly from the command prompt.
    main()