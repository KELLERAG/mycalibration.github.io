# coding: utf-8

"""
    myCalibration OpenAPI 3 Specification

    myCalibration API  # noqa: E501

    OpenAPI spec version: 1.22.178.1
    Contact: engineering@keller-pressure.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MathematicalModelPart(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'inputs': 'list[str]',
        'output': 'str',
        'description': 'str',
        'coefficients': 'list[list[float]]'
    }

    attribute_map = {
        'inputs': 'Inputs',
        'output': 'Output',
        'description': 'Description',
        'coefficients': 'Coefficients'
    }

    def __init__(self, inputs=None, output=None, description=None, coefficients=None):  # noqa: E501
        """MathematicalModelPart - a model defined in Swagger"""  # noqa: E501
        self._inputs = None
        self._output = None
        self._description = None
        self._coefficients = None
        self.discriminator = None
        if inputs is not None:
            self.inputs = inputs
        if output is not None:
            self.output = output
        if description is not None:
            self.description = description
        if coefficients is not None:
            self.coefficients = coefficients

    @property
    def inputs(self):
        """Gets the inputs of this MathematicalModelPart.  # noqa: E501

        Input variables of the model part  # noqa: E501

        :return: The inputs of this MathematicalModelPart.  # noqa: E501
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this MathematicalModelPart.

        Input variables of the model part  # noqa: E501

        :param inputs: The inputs of this MathematicalModelPart.  # noqa: E501
        :type: list[str]
        """

        self._inputs = inputs

    @property
    def output(self):
        """Gets the output of this MathematicalModelPart.  # noqa: E501

        Output variable of the model part  # noqa: E501

        :return: The output of this MathematicalModelPart.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this MathematicalModelPart.

        Output variable of the model part  # noqa: E501

        :param output: The output of this MathematicalModelPart.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def description(self):
        """Gets the description of this MathematicalModelPart.  # noqa: E501


        :return: The description of this MathematicalModelPart.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MathematicalModelPart.


        :param description: The description of this MathematicalModelPart.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def coefficients(self):
        """Gets the coefficients of this MathematicalModelPart.  # noqa: E501


        :return: The coefficients of this MathematicalModelPart.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients):
        """Sets the coefficients of this MathematicalModelPart.


        :param coefficients: The coefficients of this MathematicalModelPart.  # noqa: E501
        :type: list[list[float]]
        """

        self._coefficients = coefficients

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MathematicalModelPart, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MathematicalModelPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
