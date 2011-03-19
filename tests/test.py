

# Python standard library
import os

# This module
from imagecraft import ImageGenerator

RGB24_COLORS = {
    'red': '#FF0000',
    'yellow': '#FFFF00',
    'green': '#007700',
    'blue': '#0000AA',
    'orange': '#FF6600',
    'purple': '#9900BB',
    'white': '#FFFFFF',
    'black': '#000000',
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
}

class GeneratorTest(ImageGenerator):
    """ImageGenerator subclass for running tests."""
    _default_source_path = os.path.join(os.path.dirname(__file__), 'source')
    _default_output_path = os.path.join(os.path.dirname(__file__), 'output')
    image_format = 'PNG'


class SingleGradientTest(GeneratorTest):
    """Creates a single image gradient. Should produce a square with solid
    red in the upper-left with a gradient toward transparent at the bottom
    right."""
    output_filename = "single_gradient_test.png"
    layers = (
        {'red': 'rgba_grad_ne.png'},
    )


class DualGradientTest(GeneratorTest):
    """Overlays two differently-colored image gradients. Should produce a
    square with solid green at the upper left blending into solid red at the
    bottom right."""
    output_filename = "dual_gradient_test.png"
    layers = (
        {'red': 'rgb_solid.png'},
        {'green': 'rgba_grad_nw.png'},
    )


class QuadGradientTest(GeneratorTest):
    """Overlays two differently-colored image gradients. Should produce a
    square with white at the bottom right, blue at the bottom left,
    green at the top left and red at the top right. The center should be
    nearly transparent."""
    output_filename = "quad_gradient_test.png"
    layers = (
        {'red': 'rgba_grad_ne.png'},
        {'green': 'rgba_grad_nw.png'},
        {'blue': 'rgba_grad_sw.png'},
        {'white': 'rgba_grad_se.png'},
    )


class SolidStarTest(GeneratorTest):
    """Creates a star over a solid background color. Should produce a yellow
    star over a red background."""
    output_filename = "solid_star_test.png"
    layers = (
        {'red': 'rgb_solid.png'},
        {'yellow': 'rgba_star.png'},
    )


class AlphaStarTest(GeneratorTest):
    """Creates a star over an alpha-transparent gradient background. Should
    produce a purple star over a yellow-and-orange alpha-transparent background
    """
    output_filename = "alpha_star_test.png"
    layers = (
        {'orange': 'rgba_grad_ne.png'},
        {'yellow': 'rgba_grad_se.png'},
        {'orange': 'rgba_grad_sw.png'},
        {'yellow': 'rgba_grad_nw.png'},
        {'purple': 'rgba_star.png'},
    )


def main():
    """Runs some stupid tests"""
    for test in (SingleGradientTest, DualGradientTest, QuadGradientTest,
                 SolidStarTest, AlphaStarTest):
        test(RGB24_COLORS).render()


if __name__ == "__main__":
    main()